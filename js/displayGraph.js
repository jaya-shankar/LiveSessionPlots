var file_names = ['8.png', '4.png', '5.png', '7.png', '6.png', '2.png', '3.png', '1.png'];
document.addEventListener('DOMContentLoaded', function() {

    for (var i = 0; i < file_names.length; i++) {
        var img = document.createElement("img");
        img.src = "graphs/"+file_names[i];
        img.className = 'centerImg'
        document.body.appendChild(img);
    }

     
}
);