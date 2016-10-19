function change() // no ';' here
{
    var elem = document.getElementById("connect");
    if (elem.value=="Connect") 
	{	elem.value = "Invitation send";
		elem.style.backgroundColor="red"; 
	}
	else
	{
		elem.value = "Connect";
		elem.style.background="Cyan   ";
	}
}

function change2() // no ';' here
{
    var elem = document.getElementById("message");
    if (elem.value=="Send message") 
	{	elem.value = "Message send";
		elem.style.backgroundColor="red"
	}
	
}