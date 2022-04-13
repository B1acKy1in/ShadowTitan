package controller

import (
	"time"
)

type Clock struct {
	taskFlagChan chan int
}

func NewTimer(taskFlagChan chan int) *Clock {
	return &Clock{
		taskFlagChan: taskFlagChan,
	}
}

func (c *Clock) Worker() {
	count := int8(0)
	taskFlag := 1
	trick := time.NewTicker(3 * time.Minute)
	for range trick.C {
		// count to check if is an hour
		count++
		if count == int8(60) {
			taskFlag = taskFlag | 2
		}

		// exec trick

		c.taskFlagChan <- taskFlag

		// clear task flag
		taskFlag = taskFlag & 1
	}
}
