�	z����@z����@!z����@	S
���A?S
���A?!S
���A?"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$z����@Ե�>U��?A�[�ρ��@Y`Z�'�æ?*	8�A`��/A2~
GIterator::Model::MaxIntraOpParallelism::Prefetch::FlatMap[0]::Generator�f��a�@!��}��X@)�f��a�@1��}��X@:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelismO!W�Y�?!�X��V�c?)�n��m�?1�fyp��T?:Preprocessing2g
0Iterator::Model::MaxIntraOpParallelism::PrefetchԷ�鲈?!K�h��R?)Է�鲈?1K�h��R?:Preprocessing2p
9Iterator::Model::MaxIntraOpParallelism::Prefetch::FlatMapY�8֕a�@!ռ5=��X@)���$��`?1����)?:Preprocessing2F
Iterator::Model�V{��?!ˈ�!eae?)�VC�K_?1���O��'?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9S
���A?I��t��X@Zno#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	Ե�>U��?Ե�>U��?!Ե�>U��?      ��!       "      ��!       *      ��!       2	�[�ρ��@�[�ρ��@!�[�ρ��@:      ��!       B      ��!       J	`Z�'�æ?`Z�'�æ?!`Z�'�æ?R      ��!       Z	`Z�'�æ?`Z�'�æ?!`Z�'�æ?b      ��!       JCPU_ONLYYS
���A?b q��t��X@Y      Y@q-�2�C?"�
device�Your program is NOT input-bound because only 0.0% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)Q
Otf_data_bottleneck_analysis (find the bottleneck in the tf.data input pipeline)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*�
�<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2M
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono2no:
Refer to the TF2 Profiler FAQ2"CPU: B 