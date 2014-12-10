---
title: "iOS 开发中报错unable to dequeue a cell with identifier Cell - must register a nib or a class for the identifier or connect a prototype cell in a storyboard 的解决方法"
date: 2014-08-27 17:14
categories:
slug: ios-error-unable-to-dequeue-a-cell
---
在iOS开发中，如果遇到错误：
```
unable to dequeue a cell with identifier Cell - must register a nib or a class for the identif    ier or connect a prototype cell in a storyboard 
```
可以试试下面的解决方法。

将如下代码：
```
UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier forIndexPath:indexPath];
```
修改为如下代码：
```
 UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
```

解决方法来自[stackoverflow](http://stackoverflow.com/questions/19084274/xcode-unable-to-dequeue-a-cell-with-identifier)
