from Blog.models_blog import users,posts

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid")
    return wrapper

session={}
def authentication(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user
# print(authentication(username="akhil",password="Password@123"))

class LoginView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authentication(username=username,password=password)
        if user:
            session["user"]=user[0]
        print(session)

class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        print(kwargs)
        my_post=kwargs.get("data")
        userId=session["user"]["id"]
        my_post["userId"]=userId
        posts.append(my_post)
        # print(posts[-1])

class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post

class AddLike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post)

login=LoginView()
login.post(username="akhil",password="Password@123")

all_post=PostListView()
# print(all_post.get())

myposts=MyPostListView()
# print(myposts.get())

my_post={
    "postId":9,"title":"hello morning","content":"content","liked_by":[]
}
all_post.post(data=my_post)

like=AddLike()
like.post(postid=5)