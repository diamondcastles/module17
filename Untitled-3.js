// Array of movie ratings
var movieScores = [
    4.4,
    3.3,
    5.9,
    8.8,
    1.2,
    5.2,
    7.4,
    7.5,
    7.2,
    9.7,
    4.2,
    6.9
  ];
  
  // Starting a rating count
  var sum = 0;
  
  // Arrays to hold movie scores
  var goodMovieScores = [];
  var okMovieScores = [];
  var badMovieScores = [];
  
  // Add a for loop
  // for (let i = 0; i < cars.length; i++) {
  //   text += cars[i] + "<br>";
  // }
  
  for (let i = 0; i < movieScores.length; i++) {
    sum += movieScores[i]
    if (movieScores[i]< 4.5) {
      badMovieScores.push(movieScores[i])
    } else if (movieScores[i]>7) {
      goodMovieScores.push(movieScores[i]) 
   
    } else {okMovieScores.push(movieScores[i])} 
  }
var mean = sum /movieScores.length;
  console.log(goodMovieScores)
  console.log(okMovieScores)
  console.log(badMovieScores)
  console.log(mean)