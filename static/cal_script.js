function clean(){
    document.formc.textview.value = " " ;
};

function display(btnvalue){
    document.formc.textview.value = document.formc.textview.value + btnvalue ;
};



function deletee(){
    var del = document.formc.textview.value;
    document.formc.textview.value = del.substring(0,del.length-1);
}