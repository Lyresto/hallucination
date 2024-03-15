output = MyNet(input)
softmax = torch.nn.Softmax(dim=1)
conf = softmax(output)
confidence_score, classes = torch.max(conf, 1)
