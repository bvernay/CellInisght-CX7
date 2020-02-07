setBatchMode(true);
print("\\Clear");
dir1 = getDirectory("Choose an input Directory");
dir2 = getDirectory("Choose an output Directory");
list = getFileList(dir1);
for (i =0; i<list.length; i++){
	//print(list[i]);
	//temp = list[i];
	//lastIndex = (lengthOf(temp))-1;
	folderName = substring(list[i], 0, ((lengthOf(list[i]))-1));
	//print(folderName);
	fileList = getFileList(dir1+list[i]);
	firstfileinfolder = dir1+list[i]+fileList[0];
	well = substring(dir1, lastIndexOf(dir1, File.separator)-3, lengthOf(dir1)-1);
	run("Image Sequence...", "open="+firstfileinfolder+" sort");
	run("Flip Vertically", "stack");
	run("Make Montage...", "columns=9 rows=9 scale=1");
	saveAs("tiff", dir2+well+"_"+folderName+".tiff");
	run("Close All");
}
setBatchMode(false);