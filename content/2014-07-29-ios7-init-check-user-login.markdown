---
title: "iOS7中如何根据用户是否登录来决定是否启动Main.storyboard或登录界面"
date: 2014-07-29 10:58
categories:
slug: ios7-init-check-user-login
---
从iOS7开始，在xcode中新建一个iOS项目，默认会建立一个Main.storyboard，在项目属性中，app的启动界面默认启动这个storyboard（在general->Main Interface选项）。这样通常是方便我们开发的。减少了大量在ViewController中切换的代码。

但是，如果我们要做一个带有用户系统的app，实现如下功能：
>
app启动的时候判断用户是否已经登录，如果没有登录，显示『登录或注册界面』，如果已经登录，则显示主界面。

我们需要在AppDelegate的application: didFinishLaunchingWithOptions: 方法中去实现：

```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    if ([user logined]) {        
        UIStoryboard *storyBoard=[UIStoryboard storyboardWithName:@"Main" bundle:nil];
        mainTabBarController *mainVC = [storyBoard instantiateInitialViewController];                
        self.window.rootViewController = mainVC;
    }
    else {
        LoginPage *loginPage = [[LoginPage alloc] init];        
        self.window.rootViewController = loginPage;
    }
    return YES;
}
```
这也是在iOS6及其以前的版本中的默认做法。

