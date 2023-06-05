<%--
  Created by IntelliJ IDEA.
  User: rytter
  Date: 2022/12/20
  Time: 下午4:17
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>

<head>
    <link rel="stylesheet" href="style.css">
    <title>web安全作业（网盘）</title>
</head>

<body>
    <form action="uploadservlet" method="post" enctype="multipart/form-data">
        <div class="upload-box">
            <legend class="title">文件上传</legend>
            <div class="button_box2"><input type="file" name="file" /></div>
            <input class="button_box" type="submit" value="上传">
        </div>

    </form>
</body>

</html>