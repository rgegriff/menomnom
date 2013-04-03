// JavaScript Document

$(document).ready(function(e) {
	
	// Sets initial characters left
	$('#charsLeft').text('350');
	$('#charsLeftBulletin').text('140');
	
	// Function for blur day validation
	
	function blurState(blurClass) {	
		$('.' + blurClass + ' input').blur(function() {	
			var clone = $(this).parent().attr('id');
			var specific = $('#' + clone);
			// Check to see what Select Option val is
			var selectDefault = specific.find('select :first').val();
			var selectVal = specific.find('select :selected').val();
			if(selectVal == selectDefault) {
				specific.find('.warning').show();
			}	
		});	
	}
	
	// Day selected, remove "required text"
	
	function changeDay(whichClass) {
		$('.' + whichClass + ' select').change(function() {
		var $this = $(this).parent();
		var selected = $this.find('select :selected').val();
		var defaultVal = $this.find('select :first').val();
		
		if(selected != defaultVal) {
			$this.find('.warning').hide();
		}
		
		});
	}
	
	blurState('clonedFood');
	blurState('clonedDrink');
	changeDay('clonedFood');
	changeDay('clonedDrink');
	
	// General div creation
	
	function newDiv(whichClass,whichId) {
		var howMany = $('.' + whichClass).length;
		var newField = howMany + 1;
		var newElem = $('#' + whichId + howMany).clone().attr('id', whichId + newField);	
		newElem.children(':first').attr('id', 'name' + newField).attr('name', 'name' + newField);
		$('#' + whichId + howMany).after(newElem.fadeIn(300));
		newElem.find('.warning').hide();
		blurState(whichClass);
		changeDay(whichClass);
	}
	

	
	$('#description').elastic(); // Makes the textarea stretch
	
	$('table input').timepicker({
		timeFormat: 'hh:mm:ss',
		ampm: false
	});
    $("input[type='checkbox']").tzCheckbox();
    $("input[id$='description']").width(360);
    $("label[for$='DELETE']").hide()
    $("label[for$='description']").hide()
});