"use strict";


document.addEventListener('DOMContentLoaded', function(){

});


function get(element) {
    return document.querySelector(element);
}


function print(variable) {
    // Sorry, I just really love python =)
    console.log(variable);
}


function ajax_request() {
    $.ajax({
        url: '/function',
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            print(data);
        },
        error: function(jqxhr, status, errorMsg) {
            print(errorMsg);
        }
    });
}