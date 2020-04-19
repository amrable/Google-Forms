def script():
    customized_form = '''
function helloWorld() {
    var form = FormApp.create('New Form');
    var item = form.addCheckboxItem();
    item.setTitle('What condiments would you like on your hot dog?');
    item.setChoices([
            item.createChoice('Ketchup'),
            item.createChoice('Mustard'),
            item.createChoice('Relish')
        ]);
    form.addMultipleChoiceItem()
        .setTitle('Do you prefer cats or dogs?')
        .setChoiceValues(['Cats','Dogs'])
        .showOtherOption(true);
    form.addPageBreakItem()
        .setTitle('Getting to know you');
    form.addDateItem()
        .setTitle('When were you born?');
    form.addGridItem()
        .setTitle('Rate your interests')
        .setRows(['Cars', 'Computers', 'Celebrities'])
        .setColumns(['Boring', 'So-so', 'Interesting']);
    Logger.log('Published URL: ' + form.getPublishedUrl());
    Logger.log('Editor URL: ' + form.getEditUrl());
}
'''
    return customized_form