/****************************************************************************
** ui.h extension file, included from the uic-generated form implementation.
**
** If you want to add, delete, or rename functions or slots, use
** Qt Designer to update this file, preserving your code.
**
** You should not define a constructor or destructor in this file.
** Instead, write your code in functions called init() and destroy().
** These will automatically be called by the form's constructor and
** destructor.
*****************************************************************************/


void AbstractCategoryManager::AbstractCategoryManager_destroyed( QObject * )
{

}


void AbstractCategoryManager::buttonAdd_clicked()
{
	category = self.editCategory.text()
	try:
		self.tracker.createActivityType( category.ascii() )
		self.listCategory.insertItem( category )
		self.editCategory.clear()
	except Exception:
		pass
}


void AbstractCategoryManager::buttonDelete_clicked()
{
	category = self.editCategory.text()
	if not category.isEmpty() and self.listCategory.count != 0:
		for i in range( self.listCategory.count() ):
			if category == self.listCategory.item( i ).text():
				self.listCategory.removeItem( i )
				self.tracker.deleteActivityType( category.ascii() )
				self.editCategory.clear()
				break;

	self.listCategory.clearSelection()
}


void AbstractCategoryManager::listCategory_selected( QListBoxItem *a0 )
{
	self.editCategory.setText( a0.text() )
}


void AbstractCategoryManager::pushRename_clicked()
{
	categoryOld = self.listCategory.item( self.listCategory.currentItem() ).text()
	categoryNew =  self.editCategory.text()
	print categoryOld, categoryNew
	self.tracker.renameActivityType( categoryOld.ascii(), categoryNew.ascii() )
	self.listCategory.changeItem( categoryNew, self.listCategory.currentItem() );
	self.listCategory.clearSelection()
	self.editCategory.clear()
}
