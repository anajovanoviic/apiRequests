''' Youtube Channel : Asim Code
PyGithub repository example in Python
https://youtu.be/95Qu8icyjAk
'''
from github import Github
my_git = Github("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")
for repo in my_git.get_user().get_repos():
    print(repo.name)


asim_code = my_git.get_repo("anajovanoviic/pythonApp")
contents = asim_code.get_contents("")
for content_file in contents:
    print(content_file) 
