#!/usr/bin/env python3


import requests
import datetime


def calculate_reference_date(days):
    today_date = datetime.date.today()
    timeshift = datetime.timedelta(days=days)
    reference_date = today_date - timeshift
    return reference_date


def get_trending_repositories(top_size, reference_date):
    headers = {"Accept": "Application/JSON"}
    params = {
        "sort": "star",
        "page": "1",
        "per_page": top_size,
        "q": "created:>={}".format(reference_date)
    }
    url = "https://api.github.com/search/repositories"
    trending_repos_responce = requests.get(
        url,
        headers=headers,
        params=params
    )
    trending_repos_list = trending_repos_responce.json()["items"]
    return trending_repos_list


def get_open_issues(trending_repos_list):
    trending_repos_info_list = [
        {"name": trending_repo["full_name"], "url": trending_repo["url"]}
        for trending_repo in trending_repos_list
    ]
    trending_repos_names = [
        trending_repo_info["name"]
        for trending_repo_info in trending_repos_info_list
    ]
    headers = {"Accept": "Application/JSON"}
    params = {
        "q": "state:open repo:{}".format(" repo:".join(trending_repos_names))
    }
    url = "https://api.github.com/search/issues"
    open_issues_common_responce = requests.get(
        url,
        headers=headers,
        params=params
    )
    open_issues_common_list = open_issues_common_responce.json()["items"]
    for trending_repo_info in trending_repos_info_list:
        open_issues = []
        for open_issue in open_issues_common_list:
            if trending_repo_info["url"] == open_issue["repository_url"]:
                open_issues.append(
                    {
                        "title": open_issue["title"],
                        "url": open_issue["url"]
                    }
                )
        trending_repo_info["open_issues"] = open_issues
    return trending_repos_info_list


def print_pretty_info(trending_repos_info_list):
    print(
        "\n"
        "Список 20  самых популярных репозиториев открыты["
        "за последние 7 дней"
    )
    for trending_repo_info in trending_repos_info_list:
        repo_name = trending_repo_info["name"]
        repo_url = trending_repo_info["url"]
        open_issues_list = trending_repo_info["open_issues"]
        print(
            "\n"
            "########################################"
            "########################################"
            "\n"
            "----------------------------------------"
            "----------------------------------------"
            "\n"
            "Репозиторий: {},"
            "\n"
            "расположен {}"
            "\n"
            "----------------------------------------"
            "----------------------------------------".format(
                repo_name,
                repo_url
            )
        )
        if open_issues_list:
            print(
                "\n"
                "открытые issues:"
            )
            for issue in open_issues_list:
                print(
                    "\n"
                    "issue: {}"
                    "\n"
                    "описан {}".format(issue["title"], issue["url"])
                )
    print(
        "\n"
        "########################################"
        "########################################"
    )


if __name__ == '__main__':
    days = 7
    top_size = 20
    reference_date = calculate_reference_date(days)
    trending_repos_list = get_trending_repositories(top_size, reference_date)
    trending_repos_info_list = get_open_issues(trending_repos_list)
    print_pretty_info(trending_repos_info_list)
