for i in range(len(box_errors)):
    ax.errorbar(box_position[i], box_height[i], box_errors[i], color=c[i])
#