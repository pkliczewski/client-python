# V1alpha1DataVolumeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | DataVolumeContentType options: \&quot;kubevirt\&quot;, \&quot;archive\&quot; | [optional] 
**pvc** | [**V1PersistentVolumeClaimSpec**](V1PersistentVolumeClaimSpec.md) | PVC is a pointer to the PVC Spec we want to use | 
**source** | [**V1alpha1DataVolumeSource**](V1alpha1DataVolumeSource.md) | Source is the src of the data for the requested DataVolume | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


