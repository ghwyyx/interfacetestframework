function displayResult(){
            var x=document.getElementById("mySelect");
            return x.options[x.selectedIndex].text;
}
function showresult() {
            var text = document.getElementById("resultdata").innerText;
            var result = JSON.stringify(JSON.parse(text), null, 2);
            document.getElementById('resultdata').innerText = result;
}