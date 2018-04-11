from django.contrib.auth.models import User
# For merging user and profile forms
from django.forms import inlineformset_factory, widgets
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

import re

from .forms import UserForm
from .models import Profile, Skill, Group


def members(request):
    profiles = Profile.objects.exclude(group__isnull=True)
    if request.method == 'POST':
        text = request.POST['searchBar'].lower()
        tokens = re.split('; |, | |\n', text)

        name_results = User.objects.none()
        skill_results = Skill.objects.none()
        group_results = Group.objects.none()

        for token in tokens:
            name_results |= User.objects.filter(first_name__icontains=token) | User.objects.filter(
                last_name__icontains=token)
            skill_results |= Skill.objects.filter(title__icontains=token)
            group_results |= Group.objects.filter(title__icontains=token)

        result_profiles = [user_profile for user_profile in profiles if
                           user_profile.user in name_results or
                           any(skill in skill_results for skill in user_profile.skills.all()) or
                           any(group in group_results for group in user_profile.group.all())
                           ]

        return render(request, "userprofile/members.html", context={"profiles": result_profiles})

    return render(request, "userprofile/members.html", context={"profiles": profiles})


def skill(request, skill_title):
    skill = Skill.objects.get(title=skill_title)
    profiles = Profile.objects.filter(skills__title__icontains=skill_title, group__isnull=False).distinct()

    context = {'skill': skill, 'profiles': profiles}
    return render(request, 'userprofile/skill.html', context)


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'userprofile/profile.html', {'profile': profile})


def specific_profile(request, user_id):
    profile = get_object_or_404(User, id=user_id).profile
    profile.update()
    return render(request, 'userprofile/profile.html', {'profile': profile})



@login_required()
def edit_profile(request):
    user = request.user
    form = UserForm(instance=user)

    # This will merge the user form for name and email together with the
    # profile form. Image field is rendered with normal FileInput to make sure
    # Django doesn't add any extra fields from ClearableFileInput template.
    ProfileInlineFormset = inlineformset_factory(
        User,
        Profile,
        fields=('image','group','access_card','study','skills','duty','auto_duty'),
        widgets={'image': widgets.FileInput()},
        can_delete=False,
        can_order=False)
    formset = ProfileInlineFormset(instance=user)

    profile = get_object_or_404(Profile, user=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            # Submit changes
            form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
            if form.is_valid():
                # If form is valid, pass instance into formset, but dont commit
                # until profile form is also valid.
                created_user = form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
                if formset.is_valid():
                    # When everything looks good in both forms
                    created_user.save()
                    formset.save()
                    return redirect("/profile/")


        return render(request, 'userprofile/edit_profile.html', {'form': form, 'formset': formset, 'profile':profile})
    else:
        return redirect("/")
