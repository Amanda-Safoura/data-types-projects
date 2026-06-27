def compare_users(user1, user2):
    return {
        "common": user1 & user2,
        "only_user1": user1 - user2,
        "all": user1 | user2
    }


user_A = {
    "python",
    "machine learning",
    "data science",
    "linux"
}


user_B = {
    "python",
    "cloud",
    "docker",
    "linux"
}

comparing_result = compare_users(user_A, user_B)

print(f"""Centres d'intérêt communs: {comparing_result["common"]}
Centres d'intérêt spécifiques à user A: {comparing_result["only_user1"]}
Centres d'intérêt de user A et user B: {comparing_result["all"]}""")

if len(comparing_result["common"]) > 2:
    print("Vous devriez devenir amis")
