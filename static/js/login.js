window.onload = function() {
            var dragContainer = document.getElementById("dragContainer");
            var dragBg = document.getElementById("dragBg");
            var dragText = document.getElementById("dragText");
            var dragHandler = document.getElementById("dragHandler");

            //滑块最大偏移量
            var maxHandlerOffset = dragContainer.clientWidth - dragHandler.clientWidth; 
            //是否验证成功的标记
            var isVertifySucc = false;
            initDrag();

            function initDrag() {
                dragText.textContent = "拖动滑块验证";
                dragHandler.addEventListener("mousedown", onDragHandlerMouseDown);

                dragHandler.addEventListener("touchstart", onDragHandlerMouseDown);
            }

            function onDragHandlerMouseDown(event) {
                document.addEventListener("mousemove", onDragHandlerMouseMove);
                document.addEventListener("mouseup", onDragHandlerMouseUp);

                document.addEventListener("touchmove", onDragHandlerMouseMove);
                document.addEventListener("touchend", onDragHandlerMouseUp);
            }

            function onDragHandlerMouseMove(event) {
                /*
                html元素不存在width属性,只有clientWidth
                offsetX是相对当前元素的,clientX和pageX是相对其父元素的

                touches：表示当前跟踪的触摸操作的touch对象的数组。
                targetTouches：特定于事件目标的Touch对象的数组。
            　　changedTouches：表示自上次触摸以来发生了什么改变的Touch对象的数组。
                */
				
				//特别注意：由于translate(-50%)，所以实际的left比属性中的offsetLeft要左50%
                var left = (event.clientX || event.changedTouches[0].clientX) - dragHandler.clientWidth / 2 - dragContainer.offsetLeft + dragContainer.clientWidth / 2;
				console.log(event.clientX, dragContainer.offsetLeft);
				console.log(event)  
                if(left < 0) {
                    left = 0;
                } else if(left > maxHandlerOffset) {
                    left = maxHandlerOffset;
                    verifySucc();
                }
                dragHandler.style.left = left + "px";
                dragBg.style.width = dragHandler.style.left;
            }
            function onDragHandlerMouseUp(event) {
                document.removeEventListener("mousemove", onDragHandlerMouseMove);
                document.removeEventListener("mouseup", onDragHandlerMouseUp);

                document.removeEventListener("touchmove", onDragHandlerMouseMove);
                document.removeEventListener("touchend", onDragHandlerMouseUp);

                dragHandler.style.left = 0;
                dragBg.style.width = 0;
            }

            //验证成功
            function verifySucc() {
                isVertifySucc = true;
                dragText.textContent = "验证通过";
                dragText.style.color = "white";
                dragHandler.setAttribute("class", "dragHandlerOkBg");

                dragHandler.removeEventListener("mousedown", onDragHandlerMouseDown);
                document.removeEventListener("mousemove", onDragHandlerMouseMove);
                document.removeEventListener("mouseup", onDragHandlerMouseUp);

                dragHandler.removeEventListener("touchstart", onDragHandlerMouseDown);
                document.removeEventListener("touchmove", onDragHandlerMouseMove);
                document.removeEventListener("touchend", onDragHandlerMouseUp);
            };
        }