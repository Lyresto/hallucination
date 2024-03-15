f=lambda g:sum((i+j>threshold)*(i+j>threshold)+(i-j>threshold)*(i-j>threshold)+(i-j<threshold)*(i+j<threshold)for i,j,r in g.items())
