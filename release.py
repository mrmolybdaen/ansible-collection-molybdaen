#!/usr/bin/env python3

# Copyright: (c) 2024, Christian Siegel <molybdaen@mr42.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
    This script is just a helper to automate setting up galaxy.yml
"""

from argparse import ArgumentParser
import jinja2


def main():
    """This function runs the program to update galaxy.yml in case of a release.
    """

    # Define command line arguments
    parser = ArgumentParser(prog='Releasy.py - Generate galaxy.yml from template')
    parser.add_argument('-t', '--template', required=False, default='galaxy.yml.j2', help='Relative path to galaxy template file')
    parser.add_argument('-r', '--release', required=True, help='Name of the release')
    parser.add_argument('-m', '--email', required=False, default=None, help='Author\'s email address')
    parser.add_argument('-a', '--author', required=False, default=None, help='Author')
    parser.add_argument('-i', '--issues', required=False, default=None, help='Issue URI')
    parser.add_argument('-g', '--repository', required=False, default=None, help='Repository URI')
    parser.add_argument('-d', '--documentation', required=False, default=None, help='Documentation URI, defaults to repository')
    parser.add_argument('-p', '--homepage', required=False, default=None, help='Homepage URL, defaults to repository')

    # Parse command line arguments
    args = parser.parse_args()

    template_path = args.template
    release = args.release
    author = args.author
    if not author:
        author = 'James T. Kirk'
    email = args.email
    if not email:
        email = 'kirk@ussenterprise.gov'
    issues = args.issues
    if not issues:
        issues = 'https://issues.example.com/'
    repo = args.repository
    if not repo:
        repo = 'https://github.com/project/'
    docs = args.documentation
    if not docs:
        docs = repo
    home = args.homepage
    if not home:
        home = repo

    # Create template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
    template = env.get_template(template_path)
    galaxy_yml = template.render(release=release, author=author, email=email, issues=issues, docs=docs, homepage=home, repo=repo)

    # Save generated galaxy.yml
    with open('galaxy.yml', 'w') as f:
        f.write(galaxy_yml)
        print(galaxy_yml)



if __name__ == '__main__':
    main()