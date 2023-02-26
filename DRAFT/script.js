loadingPlaceholder='https://media1.giphy.com/media/y1ZBcOGOOtlpC/200w.gif?cid=6c09b952k65mjm5fjx7d9avsb9ku345bs5x843gavbi8arhz&rid=200w.gif&ct=g'

imageList=[]
textList=[]
count=0

function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function GenerateImage() {
  let prompt=document.getElementById("Prompt").value;
  //console.log(prompt)
  let out=JSON.stringify(prompt)
  document.getElementById("AiImage").src = loadingPlaceholder
  document.getElementById("1st").style.visibility = "hidden";
  //document.getElementById("img1").style.position = "static;"
  ajaxPostRequest("imageGen",out,ShowImage)
  
}
function ShowImage(response){
  let data=JSON.parse(response)
  //document.getElementById("AiImage").style.visibility = "visible";
  
  document.getElementById("AiImage").src=data
  document.getElementById("AiImage").style.visibility = "visible;"
  document.getElementById("AiImage").style.position = "static;"
  document.getElementById("2nd").style.visibility = "visible";
  
}


function sendSettings() {
  let p=document.getElementById("playerNum").value;
  let o={'g':0,'p':p}
  //console.log(prompt)
  let out=JSON.stringify(o)
  document.getElementById("initial").style.visibility = "hidden";

  
  ajaxPostRequest("sendSettings",out,start)
  
}
function start(response){
  document.getElementById("1st").style.visibility = "visible";
  //data=JSON.parse(response)
  //say play x its your turn.

  
  //document.getElementById("AiImage").style.visibility = "visible";
  //document.getElementById("AiImage").src=data
  //set playerNum roundGen and startbtn to hidden. unhide 
  // unhide generatebtn and startbtn
}

function guess() {
  document.getElementById("AiImage").style.visibility = "visible;"
  document.getElementById("AiImage").src = loadingPlaceholder
  let prompt=document.getElementById("s").value;
  //console.log(prompt)
  let out=JSON.stringify(prompt)
  console.log(prompt)
  document.getElementById("2nd").style.visibility = "hidden";
  ajaxPostRequest("imageGuess",out,guessed)
}
function guessed(response){
  let data=JSON.parse(response)
  if(data["end"]){
    document.getElementById("AiImage").src=data["u"]
    document.getElementById("results").style.visibility = "visible";
  }else{
  //document.getElementById("AiImage").style.visibility = "visible";
  document.getElementById("AiImage").src=data["u"]
    document.getElementById("AiImage").style.visibility = "visible;"
  document.getElementById("AiImage").style.position = "static;"
  document.getElementById("2nd").style.visibility = "visible";
  }
}
function last(){
  let out=JSON.stringify("prompt")
  ajaxPostRequest("end",out,lastDone)
}
function lastDone(response){
   let data=JSON.parse(response)
  imageList=data["iList"]
  textList=data["tList"]
  document.getElementById("endImg").src=data["urls"]
  document.getElementById("R").innerHTML=textList[0]
  document.getElementById("results").style.visibility = "hidden";
  document.getElementById("end").style.visibility = "visible";
  document.getElementById("AiImage").style.visibility = "hidden";
  document.getElementById("AiImage").style.position = "absolute";
}
function arrowleft(){
  let out=JSON.stringify("prompt")
  ajaxGetRequest("left",updatend)
}
function arrowright(){
  let out=JSON.stringify("prompt")
  ajaxGetRequest("right",updatend)
}
function nextRound(){
  let out=JSON.stringify("prompt")
  ajaxGetRequest("left",updatend)
}

function updatend(response){
  let data=JSON.parse(response)
  document.getElementById("endImg").src=data["u"]
  document.getElementById("R").innerHTML=data["p"]
}
function reset() {
  let out=JSON.stringify("prompt")
  document.getElementById("end").style.visibility = "hidden";
  document.getElementById("initial").style.visibility = "visible";
  document.getElementById("AiImage").style.visibility = "visible;"
  document.getElementById("playerNum").value=""
  document.getElementById("Prompt").value=""
  document.getElementById("s").value=""
  
  ajaxPostRequest("resetT",out,no)
}
function no(response){
  window.location.reload()
  return
}
function next(){
    if(count < imageList.length-1){
        count+=1;
        document.getElementById("endImg").src=imageList[count];
        document.getElementById("R").innerHTML=textList[count];
      console.log(textList)
    }    else {
        count=0;
        document.getElementById("endImg").src=imageList[count];
       document.getElementById("R").innerHTML=textList[count];
    }
}

function back(){
    if(count > 0){
        count-=1;
        document.getElementById("endImg").src=imageList[count];
        document.getElementById("R").innerHTML=textList[count];
    }    else {
        count=imageList.length-1;
        document.getElementById("endImg").src=imageList[count];
        document.getElementById("R").innerHTML=textList[count];
    }
}