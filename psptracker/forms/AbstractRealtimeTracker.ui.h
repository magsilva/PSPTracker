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
    if activity:
	    activity.description = QString
}


void AbstractRealtimeTracker::Start_toggled( bool )
{
    if bool == true:
	Start.setDisabled()
	Pause.setEnabled()
	Stop.setEnabled()
	activity.start()
    }
}


void AbstractRealtimeTracker::Pause_toggled( bool )
{
    activity.pause( InterruptReason.text )
}


void AbstractRealtimeTracker::Stop_toggled( bool )
{
    if bool == true:
	Start.setEnabled()
	Pause.setDisabled()
	Stop.setDisabled()
	activity.stop()
}


void AbstractRealtimeTracker::InterruptReason_textChanged()
{
    activity.reason = InterruptReason.text
}


void AbstractRealtimeTracker::TotalTime_valueChanged( const QTime & )
{
    stress.progress = ( QTime * 100 ) / DEFAULT_STRESS_TIME
}


void AbstractRealtimeTracker::AbstractRealtimeTracker_destroyed( QObject * )
{
}


void AbstractRealtimeTracker::Start_clicked()
{
    Start.setDisabled()
}
