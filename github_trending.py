#!/usr/bin/env python3


import requests
import datetime
import collections


def calculate_reference_date(days):
    today_date = datetime.date.today()
    timeshift = datetime.timedelta(days=days)
    reference_date = today_date - timeshift
    return reference_date


def get_trending_repositories(top_size, reference_date):
    params = {
        "sort": "star",
        "page": "1",
        "per_page": top_size,
        "q": "created:>={}".format(reference_date)
    }
    url = "https://api.github.com/search/repositories"
    trending_repos_responce = requests.get(
        url,
        params=params
    )
    trending_repos_list = trending_repos_responce.json()["items"]
    return trending_repos_list


def get_open_issues(trending_repos_list):
    open_issues = collections.defaultdict(list)
    trending_repos_names = [
        trending_repo["full_name"]
        for trending_repo in trending_repos_list
    ]
    params = {
        "q": "state:open repo:{}".format(" repo:".join(trending_repos_names))
    }
    url = "https://api.github.com/search/issues"
    open_issues_common_responce = requests.get(
        url,
        params=params
    )
    open_issues_common_list = open_issues_common_responce.json()["items"]
    for open_issue in open_issues_common_list:
        open_issues[open_issue["repository_url"]].append(open_issue)
    return open_issues


def print_pretty_info(trending_repos_list, open_issues):
    repo_output_template = (
        "Репозиторий: {}"
        "\n"
        "Расположен: {}"
        "\n"
        "Позиция в топе: {}"
        )
    issue_output_template = (
        "\n"
        "issue: {}"
        "\n"
        "описан: {}"
    )
    screen_width = 80
    print(
        "\n"
        "Список 20  самых популярных репозиториев открытых"
        "за последние 7 дней"
        "\n"
    )
    for position_in_top, trending_repo in enumerate(
        trending_repos_list,
        start=1
    ):
        repo_name = trending_repo["full_name"]
        repo_url = trending_repo["url"]
        print("-"*screen_width)
        print(repo_output_template.format(
            repo_name,
            repo_url,
            position_in_top
        ))
        if repo_url in open_issues.keys():
            print("\nоткрытые issues:")
            for open_issue in open_issues[repo_url]:
                print(issue_output_template.format(
                    open_issue["title"],
                    open_issue["url"]
                ))


if __name__ == '__main__':
    days = 7
    top_size = 20
    reference_date = calculate_reference_date(days)
    trending_repos_list = get_trending_repositories(top_size, reference_date)
    open_issues = get_open_issues(trending_repos_list)
    print_pretty_info(trending_repos_list, open_issues)
