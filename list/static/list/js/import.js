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
    var taskParameterName = "task";
    var taskId = getUrlParameter(taskParameterName);
    var delay = 1 * 1000;

    function poll() {
        $.ajax({
            method: "GET",
            url: "/check?id=" + taskId,
            success: function (data) {
                var progressbar = $("#progressbar");
                var title = $("#h1title");

                if (data.state === "PROGRESS") {
                    title.html("Import in progress...");

                    var percent = data.done / data.total * 100;

                    progressbar.css("width", parseInt(percent) + "%");
                    progressbar.html(parseInt(percent) + "%");

                    setTimeout(poll, delay);
                }
                else if (data.state === "SUCCESS") {
                    progressbar.css("width", "100%");
                    progressbar.html("100%");
                    progressbar.addClass("progress-bar-success");

                    title.html("Import finished");

                    var okButton = $("#okButton");
                    okButton.removeClass("disabled");
                    okButton.addClass("btn-success");
                }
            },
            error: function() {
                setTimeout(poll, delay);
            }
        })
    }

    poll();
}