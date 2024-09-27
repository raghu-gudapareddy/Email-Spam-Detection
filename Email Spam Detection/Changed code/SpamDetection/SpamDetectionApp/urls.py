from django.urls import path

from . import views

urlpatterns = [path('', views.User, name="User"),
	       path('UploadDataset.html', views.UploadDataset, name="UploadDataset"),
	       path('UploadDatasetAction', views.UploadDatasetAction, name="UploadDatasetAction"),
	       path('TrainData.html', views.TrainData, name="TrainData"),
	       path('SpamDetection.html', views.SpamDetection, name="SpamDetection"),
	       path('SpamDetectionAction', views.SpamDetectionAction, name="SpamDetectionAction"),	      
	       path('TrainDataGA', views.TrainDataGA, name="TrainDataGA"),
]