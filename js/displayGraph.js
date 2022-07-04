

var file_name = ["graphs/20-24-Higher_Secondary_fin.png",
                "graphs/20-24-Lower_Secondary_fin.png",
                "graphs/gdp_per_capita (1).png",
                "graphs/gdp_per_capita (1).png"]

const jsonData= require('./plotNames.json'); 
console.log(jsonData);

document.addEventListener('DOMContentLoaded', function() {

    fetch('./plotNames.json')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));

    
    // console.log(file_name);
    // for each file name in the array
    for (var i = 0; i < file_name.length; i++) {
        // create a new image element
        var img = document.createElement("img");
        // set the src attribute of the image to the current file name
        img.src = file_name[i];
        img.className = 'centerImg'
        // append the image to the body
        document.body.appendChild(img);
    }

     
}
);