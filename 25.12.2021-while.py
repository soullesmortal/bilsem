#kıullanıcı adı admin,şifre 123456 yazınca sisteme giriş başarılı bunların
# dışında bir şey yazınca kullanıcı adı veya şifre hatalı diyerek tekrar kullanıcı adı ve şifre uygulamayı geliştiriniz sonsuz kere soracak doğru olunca break,

a=input("kullanıcı adını giriniz girini")
b=input("şifre giriniz")
if a+b==("admin123456"):
    print("sisteme giriş başarılı")
else:
    print("sisteme giriş başarısız")
    while True:
        input("kullanıcı adı giriniz")
        input("şifre giriniz")
        if a+b==("admin123456"):
            break
            print("sisteme giriş başarılı")
