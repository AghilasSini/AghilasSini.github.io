
import os
import codecs

filelist_path='filelist_demo.txt'

filelist=[ fl.strip()  for fl in codecs.open(filelist_path,'r','utf-8')]
outfile_path="out_put.html"
with codecs.open(outfile_path,'w','utf-8') as out:
	for file_path in filelist:
		print(file_path+'.wav')
		if os.path.exists(file_path+'.wav'):
			out.write("<tr>\n" +
					"<td>{}</td>\n".format(os.path.basename(file_path))+
					"<td>\n" +
						"<p><iframe src=\"{}\" frameborder=\"0\" height=\"40\" width=\"95%\"></iframe></p> \n".format(file_path+'.txt')+
					"</td>\n"+
					"<td>\n"+
						"<audio controls=\"\">\n"+
							"<source src=\"{}\" type=\"audio/wav\">Your browser does not support the audio tag.</source>\n".format(file_path+".wav")+
						"</audio>\n"+
					"</td>\n"+
					"<td>\n"+
						"<audio controls=\"\">\n"+
							"<source src=\"{}\" type=\"audio/wav\">Your browser does not support the audio tag.</source>\n".format(file_path+'_waveglow.wav')+
						"</audio>\n"+
					"</td>\n"+		
				"</tr>\n")