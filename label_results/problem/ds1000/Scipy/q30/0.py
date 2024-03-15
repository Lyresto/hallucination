M = M + M.transpose() - sparse.diags(M.diagonal())
