var getUrlParameter = function getUrlParameter(name) {
    var url = decodeURIComponent(window.location.search.substring(1));
    var urlParameters = url.split('&');

    for (var i = 0; i < urlParameters.length; i++) {
        var parameterName = urlParameters[i].split('=');

        if (parameterName[0] === name) {
            return parameterName[1] === undefined ? true : parameterName[1];
        }
    }
};

function startPoll() {
    var taskParameterName = "pk";
    var taskId = getUrlParameter(taskParameterName);

    function poll() {
        $.ajax({
            method: "GET",
            url: "/check?pk=" + taskId,
            success: function (data) {
                var percent = data.done / data.total * 100;

                var progressbar = $("#progressbar");

                progressbar.css("width", parseInt(percent) + "%");
                progressbar.html(parseInt(percent) + "%");
            },
            complete: function () {
                setTimeout(poll, 5000);
            }
        })
    }

    poll();
}