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


void AbstractRealtimeTracker::MainForm_destroyed( QObject * )
{

}


void AbstractRealtimeTracker::ActivityManagement_clicked()
{

}


void AbstractRealtimeTracker::Description_textChanged()
{
	if self.activity:
		self.activity.description = self.Description.text.ascii()
}


void AbstractRealtimeTracker::Start_toggled( bool state)
{
	if sate == True:
		self.Start.setDisabled( state )
		self.Pause.setEnabled( state )
		self.Stop.setEnabled( state )
		self.activity.start()
}


void AbstractRealtimeTracker::Pause_toggled( bool state )
{
	self.activity.pause( self.InterruptReason.text.ascii() )
}


void AbstractRealtimeTracker::Stop_toggled( bool state )
{
    if state == True:
	self.Start.setEnabled( state )
	self.Pause.setDisabled( state )
	self.Stop.setDisabled( state )
	self.activity.stop()
}


void AbstractRealtimeTracker::InterruptReason_textChanged()
{
	self.activity.reason = self.InterruptReason.text.ascii()
}


void AbstractRealtimeTracker::TotalTime_valueChanged( const QTime &time )
{
	self.Stress.progress = ( time * 100 ) / DEFAULT_STRESS_TIME
}


void AbstractRealtimeTracker::AbstractRealtimeTracker_destroyed( QObject * )
{
}


void AbstractRealtimeTracker::Start_clicked()
{
	self.Start.setDisabled( True )
}


void AbstractRealtimeTracker::CategoryManagement_clicked()
{
	self.categoryManager.show()
}
