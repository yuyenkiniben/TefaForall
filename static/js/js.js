var width = $(window).width;
$(document).ready(function(){

    $('.slider').slider({full_width: true, height: 650});
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 300 // Creates a dropdown of 15 years to control year
    });
    $('.collapsible').collapsible();
    Materialize.updateTextFields();
    $('.modal').modal();
    $('.tooltipped').tooltip({delay: 50});

    $('.dropdown-button').dropdown({
            inDuration: 300,
            outDuration: 225,
            constrain_width: false, // Does not change width of dropdown to that of the activator
            hover: true, // Activate on hover
            gutter: 0, // Spacing from edge
            belowOrigin: true, // Displays dropdown below the button
            alignment: 'left' // Displays dropdown with edge aligned to the left of button
        }
    );
});


