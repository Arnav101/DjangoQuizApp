function startTimer() {
  var presentTime = document.getElementById('timer').innerHTML;
  var timeArray = presentTime.split(/[:]+/);
  var m = timeArray[0];
  var s = checkSecond((timeArray[1] - 1));
  if(s==59){m=m-1}
  
  document.getElementById('timer').innerHTML =
    m + ":" + s;
    document.getElementById('timeleft').value = document.getElementById('timer').innerHTML;
  console.log(m)
  if(document.getElementById('timer').innerHTML == '0:00') {
      window.location.href = 'logoff';
  }
  setTimeout(startTimer, 1000);
}

function checkSecond(sec) {
  if (sec < 10 && sec >= 0) {sec = "0" + sec}; // add zero in front of numbers < 10
  if (sec < 0) {sec = "59"};
  return sec;
}