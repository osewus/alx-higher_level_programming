#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const cha = results[i].characters;
      for (let j = 0; j < cha.length; j++) {
        if (cha[j].slice(cha[j].length - 3, cha[j].length - 1) === '18') { count += 1; }
      }
    }
    console.log(count);
  }
});

// #!/usr/bin/node

// const request = require('request');
// const url = process.argv[2];
// request.get(url, function (err, response, body) {
//   let count = 0;
//   if (err) {
//     console.log(err);
//   }
//   const data = JSON.parse(body);
//   for (let i = 0; data.results[i] !== undefined; i++) {
//     if (data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
//       count++;
//     }
//   }
//   console.log(count);
// });
