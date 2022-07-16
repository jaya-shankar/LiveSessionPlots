var file_names = ['1.png', '2.png', '3.png', '5.png', '6.png', '7.png', '8.png'];
document.addEventListener('DOMContentLoaded', function() {

    for (var i = 0; i < file_names.length; i++) {
        var img = document.createElement("img");
        img.src = "graphs/1/"+file_names[i];
        img.className = 'centerImg'
        document.body.appendChild(img);
    }

     
}
);