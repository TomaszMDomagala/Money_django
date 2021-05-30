window.onload = function () {
  
    let minutes = 0;
    let seconds = 0; 
    let milis = 0; 
    const appendMilis = document.getElementById("milis")
    const appendSeconds = document.getElementById("seconds")
    const appendMinutes = document.getElementById("minutes")
    const appendMoves = document.getElementById("scramble");
    const buttonStart = document.getElementById('start');
    const buttonStop = document.getElementById('stop');
    const buttonReset = document.getElementById('reset');
    let Interval ;
    
    makeScramble();
  
    buttonStart.onclick = function() {
      
       clearInterval(Interval);
       Interval = setInterval(startTimer, 10);
    }
    
    buttonStop.onclick = function() {
       clearInterval(Interval);
    }
    
  
    buttonReset.onclick = function() {
      clearInterval(Interval);
      milis = "00";
        seconds = "00";
      minutes = "00";
      appendMilis.innerHTML = milis;
        appendSeconds.innerHTML = seconds;
      appendMinutes.innerHTML = "";
      makeScramble();
    }
    
     
    
    function startTimer () {
      milis++; 
      
      if(milis <= 9){
        appendMilis.innerHTML = "0" + milis;
      }
      
      if (milis > 9){
        appendMilis.innerHTML = milis;
        
      } 
      
      if (milis > 99) {
        seconds++;
        appendSeconds.innerHTML = "0" + seconds;
        milis = 0;
        appendMilis.innerHTML = "0" + 0;
      }
      
      if (seconds > 9){
        appendSeconds.innerHTML = seconds;
      }
      
      if (seconds >= 60) {
        minutes++;
        appendMinutes.innerHTML = "0" + minutes + ":";
        seconds = 0;
        appendSeconds.innerHTML = "0" + 0;
      }
      
      if (minutes > 9){
        appendSeconds.innerHTML = minutes;
      }
    }
    
    function makeScramble() {
          const options = ["F ", "F' ", "F2 ", "U ", "U' ",
                          "U2 ", "L ", "L' ", "L2 ", "R ",
                          "R' ", "R2 ", "B ", "B' ", "B2 ",
                          "D ", "D' ", "D2 "];
          let numOptions = [0, 1, 2, 3, 4, 5]
          let scramble = []
          let scrambleMoves = []
          let wrong = true
  
          while (wrong) {
              scramble = []
              for (let i = 0; i < 20; i++) {
                  scramble.push(numOptions[getRandomInt(6)])
              }
  
              for (let i = 0; i < 20 - 1; i++) {
                  if (scramble[i] == scramble[i + 1]) {
                      wrong = true
                      break
                  } else {
                      wrong = false
                  }
              }
          }
  
          let move
          for (let i = 0; i < 20; i++) {
              switch (scramble[i]) {
                  case 0:
                      move = options[getRandomInt(3)]
                      scrambleMoves.push(move)
                      break
                  case 1:
                      move = options[getRandomIntBetween(3, 6)]
                      scrambleMoves.push(move)
                      break
                  case 2:
                      move = options[getRandomIntBetween(6, 9)]
                      scrambleMoves.push(move)
                      break
                  case 3:
                      move = options[getRandomIntBetween(9, 12)]
                      scrambleMoves.push(move)
                      break
                  case 4:
                      move = options[getRandomIntBetween(12, 15)]
                      scrambleMoves.push(move)
                      break
                  case 5:
                      move = options[getRandomIntBetween(15, 18)]
                      scrambleMoves.push(move)
                      break
              }
          }
          appendMoves.innerHTML = scrambleMoves.join(" ");
      }
  
      function getRandomInt(max) {
          return Math.floor(Math.random() * Math.floor(max))
      }
  
      function getRandomIntBetween(min, max) {
          return Math.floor(Math.random() * (max - min) + min)
      }
      
  }
