# Machine-Leaarning
Makine öğrenmesi günümüzün popüler dallarından biridir. Konumuz yapay zekanın bir alt dalı olan makine öğrenmesidir.
Öncelikle nedir bu makine öğrenmesi?
Makine öğrenmesi en basit tanımı ile açıkça kodlama yapmaksızın makinelerin öğrenmesidir. ML(Machine Learning) de amacımız
belli bir veri kümesi kullanılarak bir sonucu tahmin edebilmektir. Bunun en popüler örneği iris bitkisi üzerinden verilir.
İris bitkisinin birden fazla türü vardır. Programımıza bitkinin çeşitli özellikleri feature olarak verilir. En son ise bitkinin türü verilir. Ancak programlarımızı yazarken hatamızın ne olduğunu hesaplayabilmek ve oluşturacağımız modelin sadece bizim verdiğimiz veriyi ezberlemesini  önlemek için bu verilerin bir kısmını Train(eğitim) ve Test olarak ayırıcağız. Yani train datası ile eğittikten sonra hiç göstermediğimiz test datasını kullanarak modelimize tahmin yaptıracağız ve gerçek değerden farkı(Loss Function) bize hatamızı verecektir.
Her modelimizin amacı hatayı minimize etmektir. Lakin olaylar burda da bitmiyor malesef. Eğer hatamız 0 olursa ve doğruluğumuz %100 olursa burada da sorun var demektir. Bu soruna overfittig denilir. Bu sorun modelimizin elindeki veriyi ezberlediği anlamına gelmektedir. Yani modelimiz eğitim verisi içindeki değerler verilirse tam doğru sonucu verir ama hiç görmediği bir veri verirsek saçma bir değer döndürür.

Yaptığımız örneklerde bir soruna iki farklı yaklaşım ele aldık. KNN algoritması ile Karar ağacı algoritmasının başarı oranlarını test ettik. Verimiz ise bir elmanın iki özelliği(sayısal) ve  rengi(sayısal; 1:kırmızı,2:yeşil,3:sarı). En iyi  sınıflama-gruplama işlemini kimin yaptığı ise uygulamalı olarak anlatılmıştır.

