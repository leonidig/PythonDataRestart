followers = {
    "alex": ["maria", "ivan", "dima"],
    "maria": ["alex", "olga"],
    "ivan": ["dima"],
    "dima": ["alex", "maria", "ivan", "some"]
}


subs = dict()

popular = max(followers, key=lambda user: len(followers[user]))
print("Найпопулярніший:", popular)

for user, subs in followers.items():
    for sub in subs:
        if user not in followers.get(sub, []):
            print(f"{user} підписаний на {sub}, але не навзаєм")


sorted_users = sorted(followers, key=lambda u: len(followers[u]), reverse=True)
print("Топ-3:", sorted_users[:3])