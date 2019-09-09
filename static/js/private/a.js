function displayResult(){
            var x=document.getElementById("mySelect");
            return x.options[x.selectedIndex].text;
}
function showresult() {
            var text = document.getElementById("resultdata").innerText;
            var result = JSON.stringify(JSON.parse(text), null, 2);
            document.getElementById('resultdata').innerText = result;
}

function ff() {
            var pager = $('#tt').datagrid('getPager');
            pager.pagination({
                buttons: [{
                    text: "运行",
                    handler: function () {
                            var ss = [];
                            var rows = $('#tt').datagrid('getChecked');
                            for(var i=0;i<rows.length;i++){
                                var row = rows[i];
                                {#$.messager.alert('系统提示', row.methodname);#}
                                ss.push('<span>'+row.methodname+":"+row.methodtype+":"+row.methodurl+'</span>');

                            }
                            $.ajax({
                                url:"/dealallrequests/",
                                data:{'data':ss},
                                type:"post",
                                dataType:"json",
                                success:function (data) {
                                    console.log("传递成功！！");
                                }
                            });
                        }
                }, {
                    text: "删除",
                    handler: function () {
                        alert("删除");
                    }
                }, {
                    text: "保存",
                    handler: function () {
                        alert("保存");
                    }
                }]
            });
        }