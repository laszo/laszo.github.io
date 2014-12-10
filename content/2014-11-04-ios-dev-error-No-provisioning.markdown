---
title: "ios开发中报错 No provisioning profiles with a valid signing identity 或 Your account already has a valid certificate"
date: 2014-11-04 17:41
categories:
slug: ios-dev-error-No-provisioning
---

如果你在多台mac上开发ios app，在遇到下面的错误时：

```
No provisioning profiles with a valid signing identity 
```

可以尝试在“钥匙链”中删除所有ios开发相关的证书。再次在设备上调试app时，可能会遇到如下错误：

```
Your account already has a valid certificate
```

这时应在另一台mac上面，导出证书，并导入到报错的电脑上，如此应该可以解决问题。

导出方法：

1. 打开xcode，打开preferences
2. 在accounts一栏，选择相关的apple id，点击 view details
3. 导出所有的 singing identities 和 provisioning profiles。