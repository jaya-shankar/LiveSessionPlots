var file_names = ['1.png', '2.png', '3.png', '5.png', '6.png', '7.png', '8.png'];
document.addEventListener('DOMContentLoaded', function() {
    let url = window.location.href;
    let folder_name = url.substring(url.lastIndexOf('page=') + 5);
    console.log(folder_name);
    folder_name = parseInt(folder_name);
    if(isNaN(folder_name)) {
        let body = document.body;
        let h1 = document.createElement('h1');
        h1.innerHTML = 'Please as the following example \n {url}?page={page_num}.';
        body.appendChild(h1);
        return;
    }
    console.log(folder_name);
    folder_name = folder_name%10;
    if (folder_name == 0) {
        folder_name = 10;
    }
    for (var i = 0; i < file_names.length; i++) {
        var img = document.createElement("img");
        img.src = "graphs/"+folder_name+"/"+file_names[i];
        img.className = 'centerImg'
        document.body.appendChild(img);
    }

     
}
);