$(function(){
    $('ul.radio-list,ul.checklist,ul.textbox').each(function(i, el){
        var questionClass = $(this).attr('class');
        $(this).parent().addClass('question-row').addClass(questionClass);
        if (questionClass=='radio-list') {
            $(this).find('input[type="radio"]').attr('name', 'radio-question-' + i);
        }
    });

    function checkQuestion() {
        resetQuestions(true);
        var questions = $('li.question-row');
        var total_questions = questions.length;
        var correct = 0;

        questions.each(function(i, el) {
            var self = $(this);
            // Single Question.
            if (self.hasClass('radio-list')) {
                if (self.find('input[type="radio"][data-content="1"]:checked').length == 1) {
                    correct += 1;
                } else {
                    self.addClass('text-danger');
                }
            }
            // Textbox Question.
            if(self.hasClass('textbox')) {
                var reversed = "".split("").reverse().join("");
            }
        });

        showScore(correct, total_questions);
    }

    function showScore(correct, total) {
        var score = (correct / total).toFixed(2) * 100;
        var msgClass = 'alert-danger';
        if (score >= 70) {
            msgClass = 'alert-success';
        } else if (score >= 50) {
            msgClass = 'alert-warning';
        }
        $('#tg-correct-questions').text(correct + ' de ' + total);
        $('#tg-score').text(score);
        $('#tg-msg').addClass(msgClass).show();
    }
    function resetQuestions(keep) {
        $('li.question-row').removeClass('text-danger');
        $('#tg-msg').hide();
    }
    $('#check-questions').on('click', checkQuestion);
    $('#reset-questions').on('click', resetQuestions);

});