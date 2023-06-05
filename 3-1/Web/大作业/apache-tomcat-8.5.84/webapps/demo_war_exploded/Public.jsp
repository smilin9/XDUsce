<%@ page import="java.util.List" %>
<%@ page import="java.util.Iterator" %>
<%@ page import="java.io.PrintWriter" %><%--
  Created by IntelliJ IDEA.
  User: rytter
  Date: 2022/12/21
  Time: 下午9:23
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>

<head>
    <link rel="stylesheet" href="style.css">
    <title>web安全作业（网盘）</title>
</head>

<body>
    <header>
        <h1>网盘朋友圈</h1>
    </header>
    <main>
        <div id="public_text"></div>
        <article>
        <%
        List<String> filenames=(List<String>) request.getSession().getAttribute("text");
        Iterator<String> it=filenames.iterator();
        while (it.hasNext()){
            PrintWriter printWriter=response.getWriter();
            String public_text= it.next();
            %><%=public_text%><%
        }
        %>
        </article>
    </main>
    <footer>
        <form action="publicservlet" method="post" enctype="multipart/form-data">
            <div class="public_page">
                <p>发朋友圈：<input type="text" name="public_text" /></p>
                <input type="submit" value="上传" style="width:50px">
            </div>
        </form>
    </footer>
</body>

</html>