function getBotResponse() {
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
    $.get("/get", { msg: rawText }).done(function(data) {
      var botHtml = '<p class="botText"><span>' + data + "</span></p>";
      $("#chatbox").append(botHtml);
      var elem = document.getElementById('chatbox');
      elem.scrollTop = elem.scrollHeight;
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    });
  }
  $("#textInput").keypress(function(e) {
    if (e.which == 13) {
      getBotResponse();
      var elem = document.getElementById('chatbox');
      elem.scrollTop = elem.scrollHeight;
    }
  });