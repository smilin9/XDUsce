<%@ page import="java.util.List" %>
<%@ page import="java.util.Iterator" %>
<%@ page import="java.io.PrintWriter" %>
<%--
  Created by IntelliJ IDEA.
  User: rytter
  Date: 2022/12/15
  Time: 下午10:20
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>

<head>
    <link rel="stylesheet" href="style.css">
    <title>web安全作业（网盘）</title>
</head>

<body>
<div >
        <legend class="title">这是您的文件，请选择操作</legend>
        <%
        List<String> filenames=(List<String>) request.getSession().getAttribute("filenames");
        Iterator<String> it=filenames.iterator();
        String output="";
        while (it.hasNext()){
            PrintWriter printWriter=response.getWriter();
            String filename= "    "+it.next();
            String href="/demo_war_exploded/downloadservlet?filename="+filename;
            String start="<a style=\"font-size:14px\" href=\""+href+"\">";
            String end="</a>";
            output=start+filename+end+"<br/>";
            %>
        <%=output%>
        <%

        }
        %>
        <button class="button_box"><a href="publicservlet">查看朋友圈</a></button>
        <button class="button_box"><a href="Upload.jsp">上传网盘文件</a></button>
</div>
</body>

</html>