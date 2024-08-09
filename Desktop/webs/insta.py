from instaloader import Instaloader, Profile, LoginRequiredException

L=Instaloader()
username = 'candle__ride'
password = 'Aa@7441119548'

try:
    L.login(username, password)

    # Define the profile username
    PROFILE = "candle__ride"

    # Fetch the profile
    profile = Profile.from_username(L.context, PROFILE)

    # Sort posts by likes in descending order
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

    # Download posts
    for post in posts_sorted_by_likes:
        L.download_post(post, PROFILE)

except LoginRequiredException:
    print("Login required. Please check your credentials or use an authenticated session.")
except Exception as e:
    print(f"An error occurred: {e