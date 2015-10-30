$(document).ready(function () {
    $('.blog-nav').click(function(e) {     //'e' is shortcut for 'event'

        $('.blog-nav-item').removeClass('.active:after');

        var $this = $(this);
        if (!$this.hasClass('active')) {
            $this.addClass('active:');
        }
        //e.preventDefault();


    });
    var user_data_form = '#user_data_form';

$.ajax({
    url: "{% url 'create' %}",
    type: "POST",
    data: $(user_data_form).serialize(),
    success: function(data) {
        if (!(data['success'])) {
            // Here we replace the form, for the
            $(user_data_form).replaceWith(data['create']);
        }
        else {
            // Here you can show the user a success message or do whatever you need
            $(user_data_form).find('.success-message').show();
        }
    },
    error: function () {
        $(user_data_form).find('.error-message').show()
    }
});

});
